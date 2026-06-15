# vllm-project/vllm#33685: [Bug]: Step3p5ForCausalLM does not support Pipeline parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#33685](https://github.com/vllm-project/vllm/issues/33685) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Step3p5ForCausalLM does not support Pipeline parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The model stepfun-ai/Step-3.5-Flash with the architecture Step3p5ForCausalLM does not support Pipeline parallelism. Launch command: ``` CUDA_VISIBLE_DEVICES=2,0,6,1,3,4,5 VLLM_PP_LAYER_PARTITION=17,6,4,4,4,4,6 vllm serve /mnt/llms/models/stepfun-ai/Step-3.5-Flash-FP8/ \ --served-model-name step3p5-flash \ --tensor-parallel-size 1 -pp 7 \ --enable-expert-parallel \ --disable-cascade-attn \ --reasoning-parser step3p5 \ --enable-auto-tool-choice \ --tool-call-parser step3p5 \ --hf-overrides '{"num_nextn_predict_layers": 1}' \ --speculative_config '{"method": "step3p5_mtp", "num_speculative_tokens": 1}' \ --trust-remote-code \ --quantization fp8 --max-model-len auto ``` Error: `NotImplementedError: Pipeline parallelism is not supported for this model. Supported models implement the `SupportsPP` interface.` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ION=17,6,4,4,4,4,6 vllm serve /mnt/llms/models/stepfun-ai/Step-3.5-Flash-FP8/ \ --served-model-name step3p5-flash \ --tensor-parallel-size 1 -pp 7 \ --enable-expert-parallel
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Step3p5ForCausalLM does not support Pipeline parallelism bug ### Your current environment ### 🐛 Describe the bug The model stepfun-ai/Step-3.5-Flash with the architecture Step3p5ForCausalLM does not support Pipel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llelism bug ### Your current environment ### 🐛 Describe the bug The model stepfun-ai/Step-3.5-Flash with the architecture Step3p5ForCausalLM does not support Pipeline parallelism. Launch command: ``` CUDA_VISIBLE_DEVICE...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: parallel-size 1 -pp 7 \ --enable-expert-parallel \ --disable-cascade-attn \ --reasoning-parser step3p5 \ --enable-auto-tool-choice \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
