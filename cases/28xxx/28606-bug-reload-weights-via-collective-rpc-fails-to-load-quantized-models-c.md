# vllm-project/vllm#28606: [Bug]: reload_weights (via collective_rpc) Fails to Load Quantized Models Correctly, Causing Tensor Shape AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#28606](https://github.com/vllm-project/vllm/issues/28606) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: reload_weights (via collective_rpc) Fails to Load Quantized Models Correctly, Causing Tensor Shape AssertionError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. 🐞 Bug Description When the vLLM engine uses a quantized model, the initial loading of the engine works perfectly. However, when reload_weights is triggered during service runtime (in my scenario, waking the model from a "sleep" state) via collective_rpc distributed to workers, the program crashes and throws an AssertionError due to tensor shape mismatch. Logs show that vLLM attempts to load a tensor read from the weight file (e.g., torch.Size([12288, 512])) into a model parameter with a different shape but the same total number of elements (e.g., torch.Size([4096, 1536])). 2. 🔬 Key Analysis: Lost Quantization Context The root cause of this issue appears to be the loss of quantization context in the reload_weights execution path. Initial Loading: vLLM recognizes the model as a quantized model and thus uses a Quantization-Aware Loader. This loader correctly handles the weight storage layout ([12288, 512]) and reshapes/permutes it to the memory layout required by the model parameters ([4096, 1536]). Reloading: When reload_weights is called, it seemingly falls back to the default_weight_loader (as evidenced by line weight_utils.py...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: reload_weights (via collective_rpc) Fails to Load Quantized Models Correctly, Causing Tensor Shape AssertionError bug;stale ### Your current environment ### 🐛 Describe the bug 1. 🐞 Bug Description When the vLLM e...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: rs, the program crashes and throws an AssertionError due to tensor shape mismatch. Logs show that vLLM attempts to load a tensor read from the weight file (e.g., torch.Size([12288, 512])) into a model parameter with a d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ight_utils.py:810 in the logs). This default loader is unaware of the special layout of AWQ quantized models and only performs a simple shape check param.size() == loaded_weight.size(), leading to the failure. Core Evid...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , the program crashes and throws an AssertionError due to tensor shape mismatch. Logs show that vLLM attempts to load a tensor read from the weight file (e.g., torch.Size([12288, 512])) into a model parameter with a dif...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Load Quantized Models Correctly, Causing Tensor Shape AssertionError bug;stale ### Your current environment ### 🐛 Describe the bug 1. 🐞 Bug Description When the vLLM engine uses a quantized model, the initial loading of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
