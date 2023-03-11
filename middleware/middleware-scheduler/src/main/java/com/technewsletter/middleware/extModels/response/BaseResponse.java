package com.technewsletter.middleware.extModels.response;

import lombok.Data;
import lombok.ToString;

import java.io.Serializable;

@Data
@ToString
public class BaseResponse  implements Serializable {
    private Integer errorCode;
    private String errorMsg;
    private String businessMsg;
}
