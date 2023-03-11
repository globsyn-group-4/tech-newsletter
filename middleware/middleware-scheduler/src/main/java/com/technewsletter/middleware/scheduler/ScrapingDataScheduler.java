package com.technewsletter.middleware.scheduler;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.technewsletter.middleware.extModels.request.ScrapingDataEntryRequest;
import com.technewsletter.middleware.extModels.response.BaseResponse;
import com.technewsletter.middleware.util.HelperFunctions;
import com.technewsletter.middleware.util.RestInvocationUtil;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import java.io.File;
import java.io.IOException;

@Slf4j
@Component
public class ScrapingDataScheduler {

    @Autowired
    private HelperFunctions helperFunctions;

    @Autowired
    private RestInvocationUtil restInvocationUtil;

    @Scheduled(fixedRateString = "900000")
    public void run(){
        log.info("Enter Scheduler");
        ScrapingDataEntryRequest scrapingDataEntryRequest = helperFunctions.fileExtraction("blogs.json", ScrapingDataEntryRequest.class);
//        BaseResponse response = restInvocationUtil.postData("afafaf", scrapingDataEntryRequest, BaseResponse.class);
        log.info("Exit Scheduler");
    }


}
