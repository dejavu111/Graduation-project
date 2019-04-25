package com.qust.employment.po;

public class Job {
    private Integer jobid;

    private String uuid;

    private String jobname;

    private String joblocation;

    private String jobrequirements;

    private String jobsalary;

    private String jobcompany;

    private String detailUrl;

    public Integer getJobid() {
        return jobid;
    }

    public void setJobid(Integer jobid) {
        this.jobid = jobid;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid == null ? null : uuid.trim();
    }

    public String getJobname() {
        return jobname;
    }

    public void setJobname(String jobname) {
        this.jobname = jobname == null ? null : jobname.trim();
    }

    public String getJoblocation() {
        return joblocation;
    }

    public void setJoblocation(String joblocation) {
        this.joblocation = joblocation == null ? null : joblocation.trim();
    }

    public String getJobrequirements() {
        return jobrequirements;
    }

    public void setJobrequirements(String jobrequirements) {
        this.jobrequirements = jobrequirements == null ? null : jobrequirements.trim();
    }

    public String getJobsalary() {
        return jobsalary;
    }

    public void setJobsalary(String jobsalary) {
        this.jobsalary = jobsalary == null ? null : jobsalary.trim();
    }

    public String getJobcompany() {
        return jobcompany;
    }

    public void setJobcompany(String jobcompany) {
        this.jobcompany = jobcompany == null ? null : jobcompany.trim();
    }

    public String getDetailUrl() {
        return detailUrl;
    }

    public void setDetailUrl(String detailUrl) {
        this.detailUrl = detailUrl;
    }
}