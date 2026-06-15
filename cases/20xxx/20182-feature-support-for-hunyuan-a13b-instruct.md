# vllm-project/vllm#20182: [Feature]: Support for Hunyuan-A13B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#20182](https://github.com/vllm-project/vllm/issues/20182) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Hunyuan-A13B-Instruct

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Tencent released this new model: https://huggingface.co/tencent/Hunyuan-A13B-Instruct It matches bigger models on benchmarks. It has a decent size to run locally and the MoE architecture should make it pretty fast. It has 256K context too. The tencent team released a docker version compatible with vllm 0.8.5 but that image lacks the new improvements. Plus I think it doesn't have the Ampere fp8 marlin support as I can't run the fp8 quant it on a 3090 system ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ke it pretty fast. It has 256K context too. The tencent team released a docker version compatible with vllm 0.8.5 but that image lacks the new improvements. Plus I think it doesn't have the Ampere fp8 marlin support as...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: mage lacks the new improvements. Plus I think it doesn't have the Ampere fp8 marlin support as I can't run the fp8 quant it on a 3090 system ### Alternatives _No response_ ### Additional context _No response_ ### Before...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er models on benchmarks. It has a decent size to run locally and the MoE architecture should make it pretty fast. It has 256K context too. The tencent team released a docker version compatible with vllm 0.8.5 but that i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: quest ### 🚀 The feature, motivation and pitch Tencent released this new model: https://huggingface.co/tencent/Hunyuan-A13B-Instruct It matches bigger models on benchmarks. It has a decent size to run locally and the MoE...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: uggingface.co/tencent/Hunyuan-A13B-Instruct It matches bigger models on benchmarks. It has a decent size to run locally and the MoE architecture should make it pretty fast. It has 256K context too. The tencent team rele...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
