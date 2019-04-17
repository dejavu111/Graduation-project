package com.qust.employment.po;

import com.fasterxml.jackson.annotation.JsonFormat;

import java.util.Date;

public class ListInfo {
    private Integer id;

    private String uuid;

    private String detailurl;

    private String title;

    private String location;

    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    private Date date;

    private String sitename;

    private Date ctime;

    private Integer isparsed;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid == null ? null : uuid.trim();
    }

    public String getDetailurl() {
        return detailurl;
    }

    public void setDetailurl(String detailurl) {
        this.detailurl = detailurl == null ? null : detailurl.trim();
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title == null ? null : title.trim();
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location == null ? null : location.trim();
    }

    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")
    public Date getDate() {
        return date;
    }
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")
    public void setDate(Date date) {
        this.date = date;
    }

    public String getSitename() {
        return sitename;
    }

    public void setSitename(String sitename) {
        this.sitename = sitename == null ? null : sitename.trim();
    }

    public Date getCtime() {
        return ctime;
    }

    public void setCtime(Date ctime) {
        this.ctime = ctime;
    }

    public Integer getIsparsed() {
        return isparsed;
    }

    public void setIsparsed(Integer isparsed) {
        this.isparsed = isparsed;
    }
}