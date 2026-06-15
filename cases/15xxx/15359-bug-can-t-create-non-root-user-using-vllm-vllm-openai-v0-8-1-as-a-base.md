# vllm-project/vllm#15359: [Bug]: Can't create non-root user using vllm/vllm-openai:v0.8.1 as a base image

| 字段 | 值 |
| --- | --- |
| Issue | [#15359](https://github.com/vllm-project/vllm/issues/15359) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't create non-root user using vllm/vllm-openai:v0.8.1 as a base image

### Issue 正文摘录

### Your current environment U used to create a non-root user Docker image for vLLM and the following version was working fine up to v0.7.3: ``` FROM vllm/vllm-openai:v0.7.3 ENV PYTHONUNBUFFERED=1 ENV HF_HUB_CACHE=/api/models ENV HF_HOME=/api/models RUN mkdir -p /api/models/ # RUN chmod +x /api/entrypoint.sh RUN chmod 777 -R /api \ && umask 000 EXPOSE 8000 # Set user and group ARG user=appuser ARG group=appuser ARG uid=1000 ARG gid=1000 RUN groupadd -g ${gid} ${group} RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user} RUN chown ${user}:${group} /api # Switch to user USER ${uid}:${gid} ``` Today was trying to make the same with v0.8.1 and got permissions errors like this: `bash: /opt/venv/bin/vllm: /opt/venv/bin/python3: bad interpreter: Permission denied` To my understanding, in addition, `/opt/venv/bin/python3` is actually a symbolic link pointing to `/root/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/bin/python3.12` And even Dockefile modification that eventually has the following content does not work: ``` FROM vllm/vllm-openai:v0.8.1 ENV PYTHONUNBUFFERED=1 ENV HF_HUB_CACHE=/api/models ENV HF_HOME=/api/models RUN mkdir -p /api/models/ # Set user and group ARG use...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: image bug ### Your current environment U used to create a non-root user Docker image for vLLM and the following version was working fine up to v0.7.3: ``` FROM vllm/vllm-openai:v0.7.3 ENV PYTHONUNBUFFERED=1 ENV HF_HUB_C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: o v0.7.3: ``` FROM vllm/vllm-openai:v0.7.3 ENV PYTHONUNBUFFERED=1 ENV HF_HUB_CACHE=/api/models ENV HF_HOME=/api/models RUN mkdir -p /api/models/ # RUN chmod +x /api/entrypoint.sh RUN chmod 777 -R /api \ && umask 000 EXP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
