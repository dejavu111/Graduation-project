package com.qust.employment.service.Impl;

import com.qust.employment.Constant.Constants;
import com.qust.employment.mapper.JobMapper;
import com.qust.employment.po.Job;
import com.qust.employment.service.IJobService;
import com.qust.employment.utils.Utils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.List;
import java.util.Map;

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
    public String getJobList(int pageNum, String jobName, String jobLocation) {
        int pageSize = 5;
        List<Job> jobList = jobMapper.selectJob(pageNum*pageSize,pageSize,jobName,jobLocation);
        if (pageNum == 0) {
            List<Map<String, Object>> totalPages = jobMapper.selectAlltotalpages();
            if (totalPages.isEmpty()) {
                return Utils.toResultJson(Constants.FAIL_CODE, "网络繁忙", "");
            }

            double pages = Math.ceil(Double.valueOf(String.valueOf(totalPages.get(0).getOrDefault("pages", "0"))) / pageSize);

            return Utils.toResultJson(Constants.SUCCESS_CODE, "", jobList, (int) pages);
        } else {
            return Utils.toResultJson(Constants.SUCCESS_CODE, "", jobList);
        }


    }

    @Override
    public String getJobsByUUID(String uuid) {
        List<Job> jobList = jobMapper.selectJobByUUID(uuid);
        return Utils.toResultJson(Constants.SUCCESS_CODE,"",jobList);
    }
}
