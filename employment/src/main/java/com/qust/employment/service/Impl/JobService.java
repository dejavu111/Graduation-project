package com.qust.employment.service.Impl;

import com.qust.employment.Constant.Constants;
import com.qust.employment.mapper.JobMapper;
import com.qust.employment.po.Job;
import com.qust.employment.service.IJobService;
import com.qust.employment.utils.Utils;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/4 15:42
 * @description：
 * @modified By：
 * @version: $
 */
@Service
@Repository
public class JobService implements IJobService {
    @Autowired
    private JobMapper jobMapper;
    @Override
    public String getJobList(String jobName, String jobLocation) {
        List<Job> jobList = jobMapper.selectJob(jobName,jobLocation);
        return Utils.toResultJson(Constants.SUCCESS_CODE,"",jobList);
    }

    @Override
    public String getJobsByUUID(String uuid) {
        List<Job> jobList = jobMapper.selectJobByUUID(uuid);
        return Utils.toResultJson(Constants.SUCCESS_CODE,"",jobList);
    }
}
