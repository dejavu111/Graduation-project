package com.qust.employment.service;

import com.qust.employment.po.Job;

import java.util.List;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/4 15:28
 * @description：
 * @modified By：
 * @version: $
 */
public interface IJobService {
   String getJobList(String jobName, String jobLocation);

   String getJobsByUUID(String uuid);
}
