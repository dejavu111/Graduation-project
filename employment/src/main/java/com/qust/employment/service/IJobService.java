package com.qust.employment.service;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/4 15:28
 * @description：
 * @modified By：
 * @version: $
 */
public interface IJobService {
   String getJobList(int pageNum, String jobName);

   String getJobsByUUID(String uuid);
}
