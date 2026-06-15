# vllm-project/vllm#35502: [Bug]: Server hangs indefinitely during inference with Qwen3.5-27B-FP8  (vLLM nightly)

| 字段 | 值 |
| --- | --- |
| Issue | [#35502](https://github.com/vllm-project/vllm/issues/35502) |
| 状态 | open |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | install |
| Operator 关键词 | fp8 |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Server hangs indefinitely during inference with Qwen3.5-27B-FP8  (vLLM nightly)

### Issue 正文摘录

### Your current environment vLLM version: Latest nightly (vllm/vllm-openai:nightly-x86_64) OS: Linux (via Docker) GPUs: 4 x NVIDIA L40 Model: Qwen3.5-27B-FP8 Tensor Parallel Size (TP): 4 ### 🐛 Describe the bug I am using the latest vllm-openai:nightly-x86_64 Docker image to serve the Qwen3.5-27B-FP8 model on 4x L40 GPUs. The server starts up successfully without any initialization errors or warnings. However, when I send a standard chat completion request to the server, the inference hangs indefinitely. The model seems to be running for a very long time, but it returns no response and throws no errors in the console. Start the vLLM server using the latest nightly Docker image with the following command: docker run --gpus '"device=0,1,2,3"' \ -p 8000:8000 \ --ipc=host \ -v /data:/data \ vllm/vllm-openai:nightly-x86_64 \ --model /data/Qwen3.5-27B-FP8 \ -tp 4 \ --reasoning-parser qwen3 \ --served-model-name qwen3_5 (Note: Server successfully loads the model weights and starts listening on port 8000.) Send a POST request to the server: curl --noproxy '*' \ -H "Accept: application/json" \ -H "Content-type: application/json" \ -X POST \ -d '{ "model": "qwen3_5", "messages":[{ "role": "...

## 现有链接修复摘要

#36462 [Bugfix] Fix GDN in_proj_ba crash with GPTQ/FP8 and TP > 1

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: h Qwen3.5-27B-FP8 (vLLM nightly) bug ### Your current environment vLLM version: Latest nightly (vllm/vllm-openai:nightly-x86_64) OS: Linux (via Docker) GPUs: 4 x NVIDIA L40 Model: Qwen3.5-27B-FP8 Tensor Parallel Size (T...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Server hangs indefinitely during inference with Qwen3.5-27B-FP8 (vLLM nightly) bug ### Your current environment vLLM version: Latest nightly (vllm/vllm-openai:nightly-x86_64) OS: Linux (via Docker) GPUs: 4 x NVID...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: "user", "content": "hello" }], "temperature": 0.1, "stream": false }' \ http://xx.xx.xx.xx:8000/v1/chat/completions The curl request blocks forever with no output. The vLLM server logs show no crash or error messages. #...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Server hangs indefinitely during inference with Qwen3.5-27B-FP8 (vLLM nightly) bug ### Your current environment vLLM version: Latest nightly (vllm/vllm-openai:nightly-x86_64) OS: Linux (via Docker) GPUs: 4 x NVID...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36462](https://github.com/vllm-project/vllm/pull/36462) | closes_keyword | 0.95 | [Bugfix] Fix GDN in_proj_ba crash with GPTQ/FP8 and TP > 1 | Closes #35502 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
