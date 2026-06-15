# vllm-project/vllm#34812: [Bug]: GraniteMoeHybridModel not applying embedding_multiplier to input embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#34812](https://github.com/vllm-project/vllm/issues/34812) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GraniteMoeHybridModel not applying embedding_multiplier to input embeddings

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When `input_embeds` is provided to `GraniteMoeHybridModel.forward`, `hidden_state` is not scaled by `self.embedding_multiplier` ([here](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/granitemoehybrid.py#L381)). This results in garbage input to the rest of the model and garbage (often empty) results out. **Repro** ```py #!/usr/bin/env python import os import sys from vllm import LLM, SamplingParams model_name = "ibm-granite/granite-4.0-350m" if len(sys.argv) > 1: model = sys.argv[1] messages = [{"role": "user", "content": [{"type": "text", "text": "Tell me a story about a developer and their dog"}]}] sampling_params = SamplingParams(temperature=0.0, max_tokens=100) # Run in-process for easier debugging and no __main__ os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" # Use input embeds conditionally kwargs = {} if int(os.getenv("INPUT_EMBEDS", "0")): # !!!!!!!!!! If true, garbage output is generated! kwargs = {"enable_prompt_embeds": True} # Load and run llm = LLM(model_name, **kwargs) outputs = llm.chat(messages, sampling_params=sampling_params) print("------------------------------") print("Chat Resul...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bage (often empty) results out. **Repro** ```py #!/usr/bin/env python import os import sys from vllm import LLM, SamplingParams model_name = "ibm-granite/granite-4.0-350m" if len(sys.argv) > 1: model = sys.argv[1] messa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s` is provided to `GraniteMoeHybridModel.forward`, `hidden_state` is not scaled by `self.embedding_multiplier` ([here](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/granitemoehybrid.py#L381))...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: GraniteMoeHybridModel not applying embedding_multiplier to input embeddings bug ### Your current environment ### 🐛 Describe the bug When `input_embeds` is provided to `GraniteMoeHybridModel.forward`, `hidden_stat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
