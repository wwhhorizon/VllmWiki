# vllm-project/vllm#36969: [Bug]: Kimi-K2.5 output a single </think> tag in the content when "enable_thinking" is set to false

| 字段 | 值 |
| --- | --- |
| Issue | [#36969](https://github.com/vllm-project/vllm/issues/36969) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2.5 output a single </think> tag in the content when "enable_thinking" is set to false

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, Kimi-K2.5 output a single tag in the content when "enable_thinking" is set to false. Docker run script: ``` docker run -d \ --gpus all \ -v /etc/localtime:/etc/localtime \ -v /mnt/data2/ai_deploy/models/pretrained/huggingface:/root/.cache/huggingface \ -v /mnt/data2/ai_deploy/models/pretrained/modelscope:/root/.cache/modelscope \ -v ./scripts:/workspace/scripts \ -e VLLM_USE_MODELSCOPE=True \ -p 9997:8000 \ --restart always \ --ipc=host \ --name Kimi-K2.5 \ vllm/vllm-openai:v0.16.0 \ --model /root/.cache/modelscope/hub/moonshotai/Kimi-K2.5 \ --served-model-name Kimi-K2.5 \ --port 8000 \ --trust-remote-code \ --mm-encoder-tp-mode data \ --compilation_config.pass_config.fuse_allreduce_rms true \ --enable-log-requests \ --tensor-parallel-size 8 \ --disable-fastapi-docs \ --enable-auto-tool-choice \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 ``` curl ``` curl --location 'http://xxx:9997/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "model": "Kimi-K2.5", "messages": [{"role": "user", "content": "who are you"}], "temperature": 0.6, "top_p": 0.9, "stream": false, "chat_template_kwargs": {"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: a single tag in the content when "enable_thinking" is set to false. Docker run script: ``` docker run -d \ --gpus all \ -v /etc/localtime:/etc/localtime \ -v /mnt/data2/ai_deploy/models/pretrained/huggingface:/root/.cac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: --gpus all \ -v /etc/localtime:/etc/localtime \ -v /mnt/data2/ai_deploy/models/pretrained/huggingface:/root/.cache/huggingface \ -v /mnt/data2/ai_deploy/models/pretrained/modelscope:/root/.cache/modelscope \ -v ./script...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: --compilation_config.pass_config.fuse_allreduce_rms true \ --enable-log-requests \ --tensor-parallel-size 8 \ --disable-fastapi-docs \ --enable-auto-tool-choice \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
