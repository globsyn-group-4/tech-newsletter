package com.technewsletter.middleware.extModels.request;

import lombok.Data;

import java.io.Serializable;

@Data
public class BaseRequest implements Serializable {
    private String authorId;
}
