# vllm-project/vllm#21714: [Installation]: Docker image build fails for Apple Silicon using Dockerfile.cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#21714](https://github.com/vllm-project/vllm/issues/21714) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Docker image build fails for Apple Silicon using Dockerfile.cpu

### Issue 正文摘录

### Your current environment ```bash # Using M2 Max Apple Silicon (note added) docker build -f docker/Dockerfile.cpu -t vllm-local ``` errors out with ``` 830.3 /workspace/vllm/csrc/cpu/quant.cpp:21:33: error: ‘BF16Vec16’ in namespace ‘vec_op’ does not name a type; did you mean ‘FP16Vec16’? 830.3 21 | using load_vec_type = vec_op::BF16Vec16; 830.3 | ^~~~~~~~~ 830.3 | FP16Vec16 ``` The same checked out main branch builds successfully locally (on Mac OS) with `pip install -e .` ### How you are installing vllm ```sh docker build -f docker/Dockerfile.cpu -t vllm-local ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Docker image build fails for Apple Silicon using Dockerfile.cpu installation ### Your current environment ```bash # Using M2 Max Apple Silicon (note added) docker build -f docker/Dockerfile.cpu -t vllm-lo
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: u -t vllm-local ``` errors out with ``` 830.3 /workspace/vllm/csrc/cpu/quant.cpp:21:33: error: ‘BF16Vec16’ in namespace ‘vec_op’ does not name a type; did you mean ‘FP16Vec16’? 830.3 21 | using load_vec_type = vec_op::B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
