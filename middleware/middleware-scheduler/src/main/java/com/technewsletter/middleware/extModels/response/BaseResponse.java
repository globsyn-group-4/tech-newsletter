package com.technewsletter.middleware.extModels.response;

import lombok.Data;

import java.io.Serializable;

@Data
public class BaseResponse  implements Serializable {
    private String errorCode;
    private String errorMsg;
    private String businessMsg;
}
