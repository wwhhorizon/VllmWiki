# vllm-project/vllm#20013: [Bug]: v0.9.1 offline data parallel failed: AssertionError, assert coord_socket is not None

| 字段 | 值 |
| --- | --- |
| Issue | [#20013](https://github.com/vllm-project/vllm/issues/20013) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.9.1 offline data parallel failed: AssertionError, assert coord_socket is not None

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - How to produce Run llama with data_parallel.py in examples and disable expert parallel, change `enable_expert_parallel=True` to `enable_expert_parallel=False` is just ok to produce the error. https://github.com/vllm-project/vllm/blob/b6553be1bc75f046b00046a4ad7576364d03c835/examples/offline_inference/data_parallel.py#L128 I run data_parallel.py with the following cmd: ```bash python data_parallel.py --model=/Path/to/Llama-3.2-1B-Instruct --dp-size=2 --tp-size=2 --enforce-eager ``` Then it will raise an AssertionError after all dp group finish work. - Error logs ```bash Adding requests: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 200/200 [00:00<00:00, 4616.00it/s] Adding requests: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 200/200 [00:00<00:00, 4672.36it/s] Processed prompts: 100%|██████████████████████████████████████████████████████████████████████████████████████| 200/200 [00:00<00:00, 467.61it/s, est. speed inpu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ur current environment ### 🐛 Describe the bug - How to produce Run llama with data_parallel.py in examples and disable expert parallel, change `enable_expert_parallel=True` to `enable_expert_parallel=False` is just ok t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cuda;moe;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: How to produce Run llama with data_parallel.py in examples and disable expert parallel, change `enable_expert_parallel=True` to `enable_expert_parallel=False` is just ok to produce the error. https://github.com/vllm-pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
