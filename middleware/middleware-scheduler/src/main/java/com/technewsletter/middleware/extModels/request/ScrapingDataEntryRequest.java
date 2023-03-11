package com.technewsletter.middleware.extModels.request;

import com.technewsletter.middleware.extModels.misc.ScrapingData;
import lombok.Data;
import lombok.ToString;

import java.io.Serializable;
import java.util.List;

@Data
@ToString
public class ScrapingDataEntryRequest extends BaseRequest implements Serializable {
    private List<ScrapingData> data;
}
