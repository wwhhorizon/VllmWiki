# vllm-project/vllm#31959: [Usage]: Cannot Run vLLM Docker Container as Non-Root User

| 字段 | 值 |
| --- | --- |
| Issue | [#31959](https://github.com/vllm-project/vllm/issues/31959) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Cannot Run vLLM Docker Container as Non-Root User

### Issue 正文摘录

I am trying to build a docker image from the vllm/vllm-openai:v0.12.0 image which will allow me to run the vllm server as a defined non-root user and dump the log file under the ownership of the same. However, I am getting constant error during startup regarding library file access inside the container. I have attempted a brute force approach by changing ownership and permission to directories like /usr or /root. However, I am still getting similar errors. The following is my raw dockerfile, apologies for any naive approach towards the permission as I am trying to debug this issue. ``` FROM vllm/vllm-openai:v0.12.0 ARG USER_ID=2066 ARG GROUP_ID=2066 ARG USER_NAME=aiuser RUN groupadd -g ${GROUP_ID} ${USER_NAME} && \ useradd -u ${USER_ID} -g ${USER_NAME} -m ${USER_NAME} ENV USER=${USER_NAME} ENV LOGNAME=${USER_NAME} ENV HOME=/home/${USER_NAME} RUN chown -R ${USER_NAME}:${USER_NAME} /opt /usr /root /home /vllm-workspace RUN chmod -R 777 /vllm-workspace WORKDIR /home/${USER_NAME} USER ${USER_NAME} RUN mkdir -p /home/therapai/.cache/huggingface/hub RUN mkdir -p /vllm-workspace/logs COPY ./vllm_log_config.json /vllm-workspace/ COPY ./vllm_model/ /home/therapai/.cache/huggingface/hub/ ``...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: home/${USER_NAME} USER ${USER_NAME} RUN mkdir -p /home/therapai/.cache/huggingface/hub RUN mkdir -p /vllm-workspace/logs COPY ./vllm_log_config.json /vllm-workspace/ COPY ./vllm_model/ /home/therapai/.cache/huggingface/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: Cannot Run vLLM Docker Container as Non-Root User usage I am trying to build a docker image from the vllm/vllm-openai:v0.12.0 image which will allow me to run the vllm server as a defined non-root user and dump...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: server as a defined non-root user and dump the log file under the ownership of the same. However, I am getting constant error during startup regarding library file access inside the container. I have attempted a brute f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ain vllm-gpt-oss-120b | cmd.subparser_init(subparsers).set_defaults(dispatch_function=cmd.cmd) vllm-gpt-oss-120b | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm-gpt-oss-120b | File "/usr/local/lib/python3.12/dist-packages/vllm/en...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
