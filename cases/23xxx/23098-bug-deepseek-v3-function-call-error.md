# vllm-project/vllm#23098: [Bug]: Deepseek v3 function call error

| 字段 | 值 |
| --- | --- |
| Issue | [#23098](https://github.com/vllm-project/vllm/issues/23098) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | moe |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek v3 function call error

### Issue 正文摘录

### Your current environment ```text vllm 0.9.0 deepseek-v3-0324 H20-141*8 vllm docker: docker run -d --privileged=true --runtime nvidia --gpus all -p 40001:40001 --ipc=host -v /xxxx:/workspace -e "VLLM_USE_V1=1" -e "VLLM_ATTENTION_BACKEND=FLASHMLA" --name=deepseek-v3-0324-vllm xxxxx.com/vllm/vllm-openai:v0.9.0.1 --model /workspace/LLM_Weights/deepseek-ai/DeepSeek-V3-0324 --port 40001 --host 0.0.0.0 --trust-remote-code --served-model-name deepseek-v3 --enable-prefix-caching --max-model-len 131072 --gpu-memory-utilization 0.95 --tensor-parallel-size 8 --enable-chunked-prefill --enable-expert-parallel --max_num_batched_tokens 32768 --block-size 64 --enable-auto-tool-choice --tool-call-parser deepseek_v3 --chat-template /workspace/LLM_Weights/deepseek-ai/tool_chat_template_deepseekv3.jinja ``` ### 🐛 Describe the bug ```python #!/usr/bin/env python # -*- encoding: utf-8 -*- """ fun_test.py """ from openai import OpenAI def get_weather(city_name: str): response = {'count': '1', 'info': 'OK', 'infocode': '10000', 'lives': [{'adcode': '440300', 'city': '深圳市', 'humidity': '81', 'humidity_float': '81.0', 'province': '广东', 'reporttime': '2023-06-14 15:00:43', 'temperature': '29', 'temperatu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: current environment ```text vllm 0.9.0 deepseek-v3-0324 H20-141*8 vllm docker: docker run -d --privileged=true --runtime nvidia --gpus all -p 40001:40001 --ipc=host -v /xxxx:/workspace -e "VLLM_USE_V1=1" -e "VLLM_ATTENT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Deepseek v3 function call error bug;stale ### Your current environment ```text vllm 0.9.0 deepseek-v3-0324 H20-141*8 vllm docker: docker run -d --privileged=true --runtime nvidia --gpus all -p 40001:40001 --ipc=h...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: hunked-prefill --enable-expert-parallel --max_num_batched_tokens 32768 --block-size 64 --enable-auto-tool-choice --tool-call-parser deepseek_v3 --chat-template /workspace/LLM_Weights/deepseek-ai/tool_chat_template_deeps...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: HMLA" --name=deepseek-v3-0324-vllm xxxxx.com/vllm/vllm-openai:v0.9.0.1 --model /workspace/LLM_Weights/deepseek-ai/DeepSeek-V3-0324 --port 40001 --host 0.0.0.0 --trust-remote-code --served-model-name deepseek-v3 --enable...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: lization 0.95 --tensor-parallel-size 8 --enable-chunked-prefill --enable-expert-parallel --max_num_batched_tokens 32768 --block-size 64 --enable-auto-tool-choice --tool-call-parser deepseek_v3 --chat-template /workspace...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
