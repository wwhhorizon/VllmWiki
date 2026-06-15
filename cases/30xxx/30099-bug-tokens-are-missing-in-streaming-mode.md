# vllm-project/vllm#30099: [Bug]: Tokens are missing in streaming mode.

| 字段 | 值 |
| --- | --- |
| Issue | [#30099](https://github.com/vllm-project/vllm/issues/30099) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tokens are missing in streaming mode.

### Issue 正文摘录

### Your current environment Some tokens are missing on servers running with the options below. The full text in the last response of the responses api's streaming contains all the text without any missing, but the delta token received through streaming is missing some parts. ```text docker run -p 8000:8000 -it --ipc=host --gpus "device=0" vllm/vllm-openai:v0.12.0 --model openai/gpt-oss-120b --gpu-memory-utilization 0.95 --port 8000 --served-model-name gptoss120b --disable-log-request --tool-call-parser openai --enable-auto-tool-choice ``` examples ```text 1 27 streaming_output: "The world of ideas is a restless sea, each thought a wave that rises, crashes, and reshapes the shore of our understanding; as we navigate its currents, we discover that curiosity fuels the tide, imagination charts the map, and perseverance steadies the vessel, reminding us that every moment of wonder—whether sparked by a sunrise, a whispered story, or the quiet hum of a distant galaxy—holds the power to transform ordinary perception into possibility." 1 27 last_output: "The world of ideas is a restless sea, each thought a wave that rises, crashes, and reshapes the shore of our understanding; as we naviga...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: he delta token received through streaming is missing some parts. ```text docker run -p 8000:8000 -it --ipc=host --gpus "device=0" vllm/vllm-openai:v0.12.0 --model openai/gpt-oss-120b --gpu-memory-utilization 0.95 --port...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: viting each passerby to step into the day’s unwritten story, where every small gesture—a smile to a stranger, a shared, a fleeting glance—has the power to ripple outward, turning ordinary moments into the quiet miracles...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -p 8000:8000 -it --ipc=host --gpus "device=0" vllm/vllm-openai:v0.12.0 --model openai/gpt-oss-120b --gpu-memory-utilization 0.95 --port 8000 --served-model-name gptoss120b --disable-log-request --tool-call-parser openai...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tilization 0.95 --port 8000 --served-model-name gptoss120b --disable-log-request --tool-call-parser openai --enable-auto-tool-choice ``` examples ```text 1 27 streaming_output: "The world of ideas is a restless sea, eac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
