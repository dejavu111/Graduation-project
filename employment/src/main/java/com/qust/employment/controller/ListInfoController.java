package com.qust.employment.controller;

import com.qust.employment.service.IListInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/3 17:20
 * @description：
 * @modified By：
 * @version: $
 */
@RestController
public class ListInfoController {
    @Autowired
    IListInfoService iListInfoService;
    @RequestMapping(value = "/listInfo/{pageNum}")
    public String listInfo(@PathVariable int pageNum) {
        return iListInfoService.getListInfoList(pageNum);
    }
}
