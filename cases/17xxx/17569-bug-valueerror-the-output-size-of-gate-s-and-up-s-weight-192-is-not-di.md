# vllm-project/vllm#17569: [Bug]: ValueError: The output_size of gate's and up's weight = 192 is not divisible by weight quantization block_n = 128.

| 字段 | 值 |
| --- | --- |
| Issue | [#17569](https://github.com/vllm-project/vllm/issues/17569) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: The output_size of gate's and up's weight = 192 is not divisible by weight quantization block_n = 128.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (VllmWorker rank=1 pid=1410768) WARNING 05-02 07:54:19 [custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two PCIe-only GPUs. To silence this warning, specify disable_custom_all_reduce=True explicitly. (VllmWorker rank=6 pid=1410773) WARNING 05-02 07:54:19 [custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two PCIe-only GPUs. To silence this warning, specify disable_custom_all_reduce=True explicitly. (VllmWorker rank=4 pid=1410771) WARNING 05-02 07:54:19 [custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two PCIe-only GPUs. To silence this warning, specify disable_custom_all_reduce=True explicitly. (VllmWorker rank=7 pid=1410774) WARNING 05-02 07:54:19 [custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two PCIe-only GPUs. To silence this warning, specify disable_custom_all_reduce=True explicitly. (VllmWorker rank=5 pid=1410772) WARNING 05-02 07:54:19 [custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: (VllmWorker rank=6 pid=1410773) INFO 05-02 07:54:19 [cuda.py:221] Using Flash Attention backend on V1 engine. (VllmWorker rank=1 pid=1410768) INFO 05-02 07:54:19 [cuda.py:221] Using Flash Attention backend on V1 engine....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ustom allreduce is disabled because it's not supported on more than two PCIe-only GPUs. To silence this warning, specify disable_custom_all_reduce=True explicitly. (VllmWorker rank=6 pid=1410773) WARNING 05-02 07:54:19...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: of gate's and up's weight = 192 is not divisible by weight quantization block_n = 128. bug;stale ### Your current environment ### 🐛 Describe the bug ``` (VllmWorker rank=1 pid=1410768) WARNING 05-02 07:54:19 [custom_all...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: nd on V1 engine. (VllmWorker rank=6 pid=1410773) WARNING 05-02 07:54:19 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best pe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: weight = 192 is not divisible by weight quantization block_n = 128. bug;stale ### Your current environment ### 🐛 Describe the bug ``` (VllmWorker rank=1 pid=1410768) WARNING 05-02 07:54:19 [custom_all_reduce.py:136] Cus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
