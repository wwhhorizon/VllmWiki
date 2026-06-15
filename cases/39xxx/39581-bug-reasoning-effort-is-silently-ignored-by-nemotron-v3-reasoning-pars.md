# vllm-project/vllm#39581: [Bug]: `reasoning_effort` is silently ignored by nemotron_v3 reasoning parser, and `reasoning_effort: "none"` produces deceptive "hidden cost" output on Nemotron-H

| 字段 | 值 |
| --- | --- |
| Issue | [#39581](https://github.com/vllm-project/vllm/issues/39581) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `reasoning_effort` is silently ignored by nemotron_v3 reasoning parser, and `reasoning_effort: "none"` produces deceptive "hidden cost" output on Nemotron-H

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM v0.19.0, serving `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8` with `--reasoning-parser nemotron_v3`, does not honor the OpenAI-standard `reasoning_effort` field in chat completion requests. There are actually **two related bugs**: ### Bug 1 — `reasoning_effort: "low"` is silently ignored `ChatCompletionRequest` declares `reasoning_effort` as a first-class field at `vllm/entrypoints/openai/chat_completion/protocol.py:182`: ```python reasoning_effort: Literal["none", "low", "medium", "high"] | None = None ``` …and auto-injects it into `chat_template_kwargs` at `protocol.py:374`: ```python chat_template_kwargs=merge_kwargs( self.chat_template_kwargs, dict( add_generation_prompt=self.add_generation_prompt, continue_final_message=self.continue_final_message, documents=self.documents, reasoning_effort=self.reasoning_effort, # Any: if data.get("reasoning_effort") == "none": data["include_reasoning"] = False return data ``` This only flips `include_reasoning` — a response-formatting switch that hides the `reasoning` field from the response body. **The model still generates the full chain of thought.** On Nemotron-3-Super this mean...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: al reproducer Serve Nemotron-3-Super with the standard config: ```bash docker run -d --name nemotron-repro \ --gpus '"device=0,1"' --ipc=host --shm-size=16g \ -p 8095:8095 \ -v $HOME/.cache/huggingface:/root/.cache/hugg...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: the bug vLLM v0.19.0, serving `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8` with `--reasoning-parser nemotron_v3`, does not honor the OpenAI-standard `reasoning_effort` field in chat completion requests. There are actu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: se return data ``` This only flips `include_reasoning` — a response-formatting switch that hides the `reasoning` field from the response body. **The model still generates the full chain of thought.** On Nemotron-3-Super...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -parallel-size 2 --max-model-len 65536 \ --kv-cache-dtype fp8 --mamba-ssm-cache-dtype float32 \ --enable-chunked-prefill --enable-prefix-caching \ --gpu-memory-utilization 0.9 --async-scheduling \ --reasoning-parser nem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ot honor the OpenAI-standard `reasoning_effort` field in chat completion requests. There are actually **two related bugs**: ### Bug 1 — `reasoning_effort: "low"` is silently ignored `ChatCompletionRequest` declares `rea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
