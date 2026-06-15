# vllm-project/vllm#30382: [Bug]: Issues with mistralai/Ministral-3-14B-Instruct-2512

| 字段 | 值 |
| --- | --- |
| Issue | [#30382](https://github.com/vllm-project/vllm/issues/30382) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issues with mistralai/Ministral-3-14B-Instruct-2512

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi all, This issue is not present when doing inference using transformers, and I do not see relevant messages in HF comments, which makes me think this is a vllm-specific issue. I am serving ministral using the following command ``` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8090 --model ministral3_14b_instruct --tokenizer_mode mistral --config_format mistral --load_format mistral --enable-auto-tool-choice --tool-call-parser mistral --tensor-parallel-size 2 --max-model-len 32000 --gpu-memory-utilization 0.90 ``` On a docker image built using the official vllm/vllm-openai:0.12.0. The only relevant change I can think of is that I am installing mistral_common==1.8.6 explicitly in the build process. The model seems to have some kind of issue when generating responses. First starts to produce some tokens in different scripts, then it continues to degrade to complete nonsense. This seems to happen less often with closed requests, such as asking "what is a newtons disk", even in a long, multi-turn conversation (using openwebui) with several topic changes such as producing code for a simulation and explaining col...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: oing inference using transformers, and I do not see relevant messages in HF comments, which makes me think this is a vllm-specific issue. I am serving ministral using the following command ``` python3 -m vllm.entrypoint...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: relevant messages in HF comments, which makes me think this is a vllm-specific issue. I am serving ministral using the following command ``` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8090 --mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 190 **Trama Godfrey Compsente** dell'autorezza: incursioni segrete nell’archetipo visibile dei versi, come onde che si *mancoleggiano* nel gioco degli accostamenti geografici. Chi trova in sé una *scalamonaca* a leggere...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: egrade to complete nonsense. This seems to happen less often with closed requests, such as asking "what is a newtons disk", even in a long, multi-turn conversation (using openwebui) with several topic changes such as pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
