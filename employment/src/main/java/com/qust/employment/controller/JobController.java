package com.qust.employment.controller;

import com.qust.employment.service.IJobService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/3 17:28
 * @description：
 * @modified By：
 * @version: $
 */
@RestController
public class JobController {
    @Autowired
    IJobService iJobService;
    @RequestMapping(value = "/job")
    public String getJobs(@RequestParam(value = "jobName") String jobName,@RequestParam(value = "jobLocation") String jobLocation) {
        return iJobService.getJobList(jobName,jobLocation);
    }
}
