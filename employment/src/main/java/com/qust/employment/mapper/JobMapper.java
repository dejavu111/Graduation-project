package com.qust.employment.mapper;

import com.qust.employment.po.Job;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;
@Mapper
public interface JobMapper {

    int deleteByPrimaryKey(Integer jobid);

    int insert(Job record);

    int insertSelective(Job record);

    Job selectByPrimaryKey(Integer jobid);

    int updateByPrimaryKeySelective(Job record);

    int updateByPrimaryKey(Job record);

    List<Job> selectJob(@Param("jobName") String jobName, @Param("jobLocation") String jobLocation);
}