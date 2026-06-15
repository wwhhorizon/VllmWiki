# vllm-project/vllm#11398: [Installation]: cannot install vllm with openvino backend

| 字段 | 值 |
| --- | --- |
| Issue | [#11398](https://github.com/vllm-project/vllm/issues/11398) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: cannot install vllm with openvino backend

### Issue 正文摘录

### Your current environment ```text ERROR: Cannot install openvino-tokenizers[transformers]==2024.4.0.0, optimum-intel and vllm==0.6.3.dev100+g15986f59.openvino because these package versions have conflicting dependencies. The conflict is caused by: vllm 0.6.3.dev100+g15986f59.openvino depends on transformers>=4.45.0 openvino-tokenizers[transformers] 2024.4.0.0 depends on transformers>=4.36.0; extra == "transformers" ``` ### How you are installing vllm ```sh git clone https://github.com/vllm-project/vllm.git cd vllm pip install -r requirements-build.txt --extra-index-url https://download.pytorch.org/whl/cpu PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cpu" VLLM_TARGET_DEVICE=openvino python -m pip install -v . follow the offical step https://docs.vllm.ai/en/latest/getting_started/openvino-installation.html ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: cannot install vllm with openvino backend installation ### Your current environment ```text ERROR: Cannot install openvino-tokenizers[transformers]==2024.4.0.0, optimum-intel and vllm==0.6.3.dev100+g15986
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Installation]: cannot install vllm with openvino backend installation ### Your current environment ```text ERROR: Cannot install openvino-tokenizers[transformers]==2024.4.0.0, optimum-intel and vllm==0.6.3.dev100+g1598...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: on -m pip install -v . follow the offical step https://docs.vllm.ai/en/latest/getting_started/openvino-installation.html ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
