package com.qust.employment.controller;

import com.qust.employment.service.IJobService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
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
    @RequestMapping(value = "/job/{pageNum}")
    public String getJobs(@PathVariable int pageNum, @RequestParam(value = "jobName",required = false,defaultValue = "") String jobName, @RequestParam(value = "jobLocation",required = false,defaultValue = "") String jobLocation) {
        return iJobService.getJobList(pageNum,jobName,jobLocation);
    }

    @RequestMapping(value = "/job/detail")
    public String getJobsByID(@RequestParam(value = "uuid") String uuid) {
        return iJobService.getJobsByUUID(uuid);
    }
}
