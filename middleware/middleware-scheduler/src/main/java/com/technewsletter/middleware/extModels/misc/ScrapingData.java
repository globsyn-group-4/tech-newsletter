package com.technewsletter.middleware.extModels.misc;

import lombok.Data;
import lombok.ToString;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.Date;

@Data
@ToString
public class ScrapingData implements Serializable {
    private String companyID;
    private Date publishedDate;
    private String header;
    private String blogName;
    private String articleUrl;
}
