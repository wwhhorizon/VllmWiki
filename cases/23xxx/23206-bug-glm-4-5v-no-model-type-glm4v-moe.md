# vllm-project/vllm#23206: [Bug]: glm-4.5v no model type 'glm4v_moe'

| 字段 | 值 |
| --- | --- |
| Issue | [#23206](https://github.com/vllm-project/vllm/issues/23206) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: glm-4.5v no model type 'glm4v_moe'

### Issue 正文摘录

### Your current environment Environments ```text PyTorch version : 2.7.1+cu128 transformers version : 4.55.2 vllm : 0.10.1rc2.dev51+g80141bbf2 ``` ### 🐛 Describe the bug Got ValueError when serving vllm. Error: ``` Value error, The checkpoint you are trying to load has model type `glm4v_moe` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. ``` Command: ``` VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=4,5,6,7 vllm serve zai-org/GLM-4.5V --tensor-parallel-size 4 --tool-call-parser glm45 --reasoning-parser glm45 --enable-auto-tool-choice --served-model-name glm-4.5v --media-io-kwargs '{"video": {"num_frames": -1}}' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: load has model type `glm4v_moe` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. ``` Command: ``` VLLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m4v_moe' bug ### Your current environment Environments ```text PyTorch version : 2.7.1+cu128 transformers version : 4.55.2 vllm : 0.10.1rc2.dev51+g80141bbf2 ``` ### 🐛 Describe the bug Got ValueError when serving vllm. E...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: glm-4.5v no model type 'glm4v_moe' bug ### Your current environment Environments ```text PyTorch version : 2.7.1+cu128 transformers version : 4.55.2 vllm : 0.10.1rc2.dev51+g80141b
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: glm-4.5v no model type 'glm4v_moe' bug ### Your current environment Environments ```text PyTorch version : 2.7.1+cu128 transformers version : 4.55.2 vllm : 0.10.1rc2.dev51+g80141bbf2 ``` ### 🐛 Des
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
