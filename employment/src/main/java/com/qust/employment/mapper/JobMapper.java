package com.qust.employment.mapper;

import com.qust.employment.po.Job;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;

@Mapper
public interface JobMapper {

    int deleteByPrimaryKey(Integer jobid);

    int insert(Job record);

    int insertSelective(Job record);

    Job selectByPrimaryKey(Integer jobid);

    int updateByPrimaryKeySelective(Job record);

    int updateByPrimaryKey(Job record);

    List<Job> selectJob(@Param("pageNum") int pageNum, @Param("pageSize") int pageSize, @Param("jobName") String jobName, @Param("jobLocation") String jobLocation);

    List<Job> selectJobByUUID(@Param("uuid") String uuid);

    List<Map<String, Object>> selectAlltotalpages();
}