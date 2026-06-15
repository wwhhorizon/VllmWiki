# vllm-project/vllm#25626: [Bug]: How to debug why child process become defunct process when using vllm deploy LLM model

| 字段 | 值 |
| --- | --- |
| Issue | [#25626](https://github.com/vllm-project/vllm/issues/25626) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: How to debug why child process become defunct process when using vllm deploy LLM model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The child process to serve model service has to be defunct process, also main process still running for serving. 1) should use some process manager(for example tini) to avoid the problem 2) how to debug the issues as no error log for why child process exit ``` UID PID PPID C STIME TTY TIME CMD root 1 0 1 Sep08 ? 06:22:55 python3 -m vllm.entrypoints.openai.api_server --model /mnt/LLM/Qwen/Qwen2.5-32B-Instruct --served-model-name Qwen2.5-32B-Instruct --enable-prefix-caching --trust-remote-code --enable root 150 1 0 Sep08 ? 00:00:00 [python3] root 151 1 20 Sep08 ? 3-09:11:51 [python3] root 225 1 99 Sep08 ? 17-02:31:11 [python3] root 244 1 99 Sep08 ? 17-02:17:59 [python3] root 302 1 0 Sep08 ? 00:00:00 [python3] root 765 0 0 01:44 pts/0 00:00:00 /bin/sh -c TERM=xterm-256color; export TERM; LANG=C.utf8; export LANG; [ -x /bin/bash ] && ([ -x /usr/bin/script ] && /usr/bin/script -q -c "/bin/bash" /dev/null || exec /bin/bash) | root 771 765 0 01:44 pts/0 00:00:00 /bin/sh -c TERM=xterm-256color; export TERM; LANG=C.utf8; export LANG; [ -x /bin/bash ] && ([ -x /usr/bin/script ] && /usr/bin/script -q -c "/bin/bash" /dev/null || exec /bin/ba...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ebug why child process become defunct process when using vllm deploy LLM model bug;stale ### Your current environment ### 🐛 Describe the bug The child process to serve model service has to be defunct process, also main...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: hild process become defunct process when using vllm deploy LLM model bug;stale ### Your current environment ### 🐛 Describe the bug The child process to serve model service has to be defunct process, also main process st...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
