# vllm-project/vllm#27385: [Bug]: gptoss calls built-in tool when no tools are given

| 字段 | 值 |
| --- | --- |
| Issue | [#27385](https://github.com/vllm-project/vllm/issues/27385) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gptoss calls built-in tool when no tools are given

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Environment vllm==0.11.0 ## Checkpoint lmsys/gpt-oss-120b-bf16 ## Deployment ``` vllm serve /home/t2vg-a100-G4-37/t2vgusw2_ryang/DeepResearch/model_cache/gpt-oss-120b-bf16 \ --tensor-parallel-size 4 \ --async-scheduling \ --served-model-name gptoss \ --reasoning-parser openai_gptoss \ --tool-call-parser openai \ --enable-auto-tool-choice ``` ## Issue I want to benchmark the model on HLE without tools, but the model tries to call built-in search tool. I'm not sure if this is an expected behavior or a bug in system prompt. I'm using chat completions api. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory cuda;triton build_error dtype;env_dependenc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ckpoint lmsys/gpt-oss-120b-bf16 ## Deployment ``` vllm serve /home/t2vg-a100-G4-37/t2vgusw2_ryang/DeepResearch/model_cache/gpt-oss-120b-bf16 \ --tensor-parallel-size 4 \ --async-scheduling \ --served-model-name gptoss \...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e the bug ## Environment vllm==0.11.0 ## Checkpoint lmsys/gpt-oss-120b-bf16 ## Deployment ``` vllm serve /home/t2vg-a100-G4-37/t2vgusw2_ryang/DeepResearch/model_cache/gpt-oss-120b-bf16 \ --tensor-parallel-size 4 \ --asy...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gptoss calls built-in tool when no tools are given bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug ## Environment vllm==0.11.0 ## Checkpoint lmsys/gpt-oss-120b-bf16 ## Deployment ``` vllm se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: gptoss calls built-in tool when no tools are given bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug ## Environment vllm==0.11.0 ## Checkpoint lmsys/gpt-oss-120b-bf16 ## Deployment ``` vllm se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
