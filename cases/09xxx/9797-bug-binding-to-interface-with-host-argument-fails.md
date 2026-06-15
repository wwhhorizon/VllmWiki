# vllm-project/vllm#9797: [Bug]: Binding to interface with `--host` argument fails

| 字段 | 值 |
| --- | --- |
| Issue | [#9797](https://github.com/vllm-project/vllm/issues/9797) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Binding to interface with `--host` argument fails

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `--host` argument for `vllm serve` is ignored. Example: ```bash /opt/vllm/.venv/bin/vllm serve --host 127.0.0.1 --port 8080 meta-llama/Llama-3.2-3B --max_model_len 8192 ... INFO: Application startup complete. INFO: Uvicorn running on socket ('0.0.0.0', 8080) (Press CTRL+C to quit) ``` This can also be confirmed with `ss`: ``` ss -tlpen | grep 8080 LISTEN 0 2048 0.0.0.0:8080 0.0.0.0:* users:(("pt_main_thread",pid=404153,fd=27),("pt_main_thread",pid=404153,fd=13)) ino:3447282 sk:6005 cgroup:/user.slice/user-2104.slice/session-2381.scope ``` The `--port` argument is respected though. I tried to connect to the public interface from the outside and this also works. That means that the host argument is totally ignored. Also, the default bind interface for such a service should NOT be `0.0.0.0` but `127.0.0.1`. IMHO this is a critical issue as this can lead to unauthorized access to system resources. The `--host` argument is listed in the [quickstart guide](https://docs.vllm.ai/en/v0.6.0/getting_started/quickstart.html#openai-compatible-server) and therefore seems to have some relevance. ### Befor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ce with `--host` argument fails bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `--host` argument for `vllm serve` is ignored. Example: ```bash /opt/vllm/.venv/bin/vllm se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
