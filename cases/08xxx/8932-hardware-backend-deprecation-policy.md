# vllm-project/vllm#8932: Hardware Backend Deprecation Policy

| 字段 | 值 |
| --- | --- |
| Issue | [#8932](https://github.com/vllm-project/vllm/issues/8932) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Hardware Backend Deprecation Policy

### Issue 正文摘录

### Anything you want to discuss about vllm. vLLM heavily depends on PyTorch, and also actively works with PyTorch team to leverage their new features. When a new PyTorch version comes out, vLLM usually upgrades to the latest PyTorch directly. Meanwhile, vLLM supports diverse hardware backends from different vendors. They often require their own PyTorch versions. In order to speed up the development of vLLM, hereby we require all vendors to keep up with PyTorch. Starting from PyTorch 2.5 (Release Day (10/17/24)), vLLM will drop hardware support if it cannot support PyTorch 2.5. potentially affected vendors and the current PyTorch version they require: - neuron (2.1.2) - openvino (2.1.2) - intel xpu (2.3.1) Note that latest pytorch support is a necessary condition for vLLM's hardware vendors. It is not sufficient. The vLLM team considers adding new hardware support depending on the community interest, the priority of the main branch, and the bandwidth of the team. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ks with PyTorch team to leverage their new features. When a new PyTorch version comes out, vLLM usually upgrades to the latest PyTorch directly. Meanwhile, vLLM supports diverse hardware backends from different vendors....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Hardware Backend Deprecation Policy stale ### Anything you want to discuss about vllm. vLLM heavily depends on PyTorch, and also actively works with PyTorch team to leverage their new features. When a new PyTorch versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: am. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Hardware Backend Deprecation Policy stale ### Anything you want to discuss about vllm. vLLM heavily depends on PyTorch, and also actively works with PyTorch team to leverage their new features. When a new PyTorch versio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s. When a new PyTorch version comes out, vLLM usually upgrades to the latest PyTorch directly. Meanwhile, vLLM supports diverse hardware backends from different vendors. They often require their own PyTorch versions. In...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
