package com.technewsletter.middleware.util;

import com.technewsletter.middleware.extModels.request.BaseRequest;
import com.technewsletter.middleware.extModels.response.BaseResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.client.SimpleClientHttpRequestFactory;
import org.springframework.web.client.RestTemplate;

@Configuration
@Slf4j
public class RestInvocationUtil {

    public <T extends BaseResponse, U extends BaseRequest> T postData(String url, U request, Class<T> clazz){
        SimpleClientHttpRequestFactory simpleClientHttpRequestFactory = new SimpleClientHttpRequestFactory();
        simpleClientHttpRequestFactory.setConnectTimeout(3000);
        simpleClientHttpRequestFactory.setReadTimeout(3000);
        RestTemplate restTemplate = new RestTemplate(simpleClientHttpRequestFactory);
        log.info("Entering rest handler");
        T t = restTemplate.postForObject(url, request, clazz);
        log.info("Data from response -> {}",t.toString());
        log.info("Exiting rest handler");
        return t;
    }
}
