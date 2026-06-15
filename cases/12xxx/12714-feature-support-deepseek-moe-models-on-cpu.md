# vllm-project/vllm#12714: [Feature]: Support DeepSeek MoE models on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#12714](https://github.com/vllm-project/vllm/issues/12714) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support DeepSeek MoE models on CPU

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, I attempted to run Deepseek-V2-Lite-Instruct in CPU mode and encountered an `AssertionError: Torch not compiled with CUDA enabled`. I noticed that in `rotary_embedding.py` on line 647, the device is explicitly set to "cuda": ```python def _compute_inv_freq(self, scaling_factor: float) -> torch.Tensor: pos_freqs = self.base**(torch.arange( 0, self.rotary_dim, 2, dtype=torch.float, device="cuda") / self.rotary_dim) ``` Is there any plan to support this operation on CPU in future releases? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: -Lite-Instruct in CPU mode and encountered an `AssertionError: Torch not compiled with CUDA enabled`. I noticed that in `rotary_embedding.py` on line 647, the device is explicitly set to "cuda": ```python def _compute_i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: in CPU mode and encountered an `AssertionError: Torch not compiled with CUDA enabled`. I noticed that in `rotary_embedding.py` on line 647, the device is explicitly set to "cuda": ```python def _compute_inv_freq(self, s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support DeepSeek MoE models on CPU feature request;stale ### 🚀 The feature, motivation and pitch Hello, I attempted to run Deepseek-V2-Lite-Instruct in CPU mode and encountered an `AssertionError: Torch not c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: pos_freqs = self.base**(torch.arange( 0, self.rotary_dim, 2, dtype=torch.float, device="cuda") / self.rotary_dim) ``` Is there any plan to support this operation on CPU in future releases? ### Alternatives _No response_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support DeepSeek MoE models on CPU feature request;stale ### 🚀 The feature, motivation and pitch Hello, I attempted to run Deepseek-V2-Lite-Instruct in CPU mode and encountered an `AssertionError: Torch not c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
