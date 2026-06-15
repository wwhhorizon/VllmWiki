# vllm-project/vllm#27266: [Bug]: Mistral text only model trigger multimodal setup that fails

| 字段 | 值 |
| --- | --- |
| Issue | [#27266](https://github.com/vllm-project/vllm/issues/27266) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral text only model trigger multimodal setup that fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve --served-model-name model --dtype bfloat16 --api-server-count 1 mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tensor-parallel-size 2 --tokenizer-mode mistral ... ERROR 10-21 10:33:29 [multiproc_executor.py:597] File "/home/mila/d/delaunap/conda/envs/py312/lib/python3.12/site-packages/transformers/models/pixtral/processing_pixtral.py", line 110, in __init__ ERROR 10-21 10:33:29 [multiproc_executor.py:597] self.image_token_id = tokenizer.convert_tokens_to_ids(self.image_token) ERROR 10-21 10:33:29 [multiproc_executor.py:597] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 10-21 10:33:29 [multiproc_executor.py:597] AttributeError: 'MistralTokenizer' object has no attribute 'convert_tokens_to_ids'. Did you mean: 'convert_tokens_to_string'? ERROR 10-21 10:33:29 [multiproc_executor.py:597] ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;ope...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: t ### 🐛 Describe the bug ``` vllm serve --served-model-name model --dtype bfloat16 --api-server-count 1 mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tensor-parallel-size 2 --tokenizer-mode mistral ... ERROR 10-21 10:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: model-name model --dtype bfloat16 --api-server-count 1 mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tensor-parallel-size 2 --tokenizer-mode mistral ... ERROR 10-21 10:33:29 [multiproc_executor.py:597] File "/home/mil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Mistral text only model trigger multimodal setup that fails bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve --served-model-name model --dtype bfloat16 --api-server-count 1 mistralai/Mistral...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
