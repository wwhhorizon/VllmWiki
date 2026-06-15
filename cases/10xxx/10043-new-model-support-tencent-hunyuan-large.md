# vllm-project/vllm#10043: [New Model]: Support Tencent-Hunyuan-Large

| 字段 | 值 |
| --- | --- |
| Issue | [#10043](https://github.com/vllm-project/vllm/issues/10043) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support Tencent-Hunyuan-Large

### Issue 正文摘录

### The model to consider. https://huggingface.co/tencent/Tencent-Hunyuan-Large Tencent released a 389B MoE with only 52B activated parameters which beats the Llama 3.1 405B. There are three checkpoints in the model card: Pretrain, Instruct, and Instruct-FP8 (AutoFP8 format) Some notable features of the model: - **High-Quality Synthetic Data**: By enhancing training with synthetic data, Hunyuan-Large can learn richer representations, handle long-context inputs, and generalize better to unseen data. - **KV Cache Compression**: Utilizes Grouped Query Attention (GQA) and Cross-Layer Attention (CLA) strategies to significantly reduce memory usage and computational overhead of KV caches, improving inference throughput. - **Expert-Specific Learning Rate Scaling**: Sets different learning rates for different experts to ensure each sub-model effectively learns from the data and contributes to overall performance. - **Long-Context Processing Capability**: The pre-trained model supports text sequences up to 256K, and the Instruct model supports up to 128K, significantly enhancing the ability to handle long-context tasks. - **Extensive Benchmarking**: Conducts extensive experiments across va...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Support Tencent-Hunyuan-Large new-model;stale ### The model to consider. https://huggingface.co/tencent/Tencent-Hunyuan-Large Tencent released a 389B MoE with only 52B activated parameters which beats the L...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: emory usage and computational overhead of KV caches, improving inference throughput. - **Expert-Specific Learning Rate Scaling**: Sets different learning rates for different experts to ensure each sub-model effectively...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ata and contributes to overall performance. - **Long-Context Processing Capability**: The pre-trained model supports text sequences up to 256K, and the Instruct model supports up to 128K, significantly enhancing the abi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ://huggingface.co/tencent/Tencent-Hunyuan-Large Tencent released a 389B MoE with only 52B activated parameters which beats the Llama 3.1 405B. There are three checkpoints in the model card: Pretrain, Instruct, and Instr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: table features of the model: - **High-Quality Synthetic Data**: By enhancing training with synthetic data, Hunyuan-Large can learn richer representations, handle long-context inputs, and generalize better to unseen data...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
