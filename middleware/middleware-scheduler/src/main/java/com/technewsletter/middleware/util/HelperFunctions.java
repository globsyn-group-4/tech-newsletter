package com.technewsletter.middleware.util;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.technewsletter.middleware.extModels.request.ScrapingDataEntryRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Configuration;

import java.io.File;
import java.io.IOException;

@Configuration
@Slf4j
public class HelperFunctions {
    public <T> T fileExtraction(String s, Class<T> clazz) {
        log.info("Entering extraxtion method");
        File file = new File(new StringBuilder().append("src/main/resources/").append(s).toString());
        ObjectMapper mapper = new ObjectMapper();
        T t = null;
        mapper.disable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        try {
            t = mapper.readValue(file, clazz);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        log.info("Object ->"+t.toString());
        log.info("Exiting extraction method");
        return t;
    }
}
