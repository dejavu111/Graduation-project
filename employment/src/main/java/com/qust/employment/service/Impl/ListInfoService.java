package com.qust.employment.service.Impl;

import com.qust.employment.Constant.Constants;
import com.qust.employment.mapper.ListInfoMapper;
import com.qust.employment.po.ListInfo;
import com.qust.employment.service.IListInfoService;
import com.qust.employment.utils.Utils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.List;
import java.util.Map;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/4 14:24
 * @description：
 * @modified By：
 * @version: $
 */
@Service
public class ListInfoService implements IListInfoService {

    @Autowired
    ListInfoMapper listInfoMapper;
    @Override
    public String getListInfoList(int pageNum) {
        int pageSize = 5;
        List<ListInfo> listInfos = listInfoMapper.selectAll(new Date(),pageNum*pageSize,pageSize);

        if (pageNum == 0) {
            List<Map<String, Object>> totalPages = listInfoMapper.selectAlltotalpages(new Date());
            if (totalPages.isEmpty()) {
                return Utils.toResultJson(Constants.FAIL_CODE, "网络繁忙", "");
            }

            double pages = Math.ceil(Double.valueOf(String.valueOf(totalPages.get(0).getOrDefault("pages", "0"))) / pageSize);

            return Utils.toResultJson(Constants.SUCCESS_CODE, "", listInfos, (int) pages);
        } else {
            return Utils.toResultJson(Constants.SUCCESS_CODE, "", listInfos);
        }
    }
}
