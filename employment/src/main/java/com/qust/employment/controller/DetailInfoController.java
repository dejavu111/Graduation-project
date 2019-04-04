package com.qust.employment.controller;

import com.qust.employment.service.IDetailInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/3 16:48
 * @description：
 * @modified By：
 * @version: $
 */
@RestController
public class DetailInfoController {
    @Autowired
    private IDetailInfoService idetailInfoService;

    @RequestMapping(value = "/detailInfo/{detailId}")
    public String detailInfo(@PathVariable("detailId") Integer detailId) {
        return idetailInfoService.getDetailInfo(detailId);
    }
}
