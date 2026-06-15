# vllm-project/vllm#3306: flash_attn is installed, but "flash_attn is not found. Using xformers backend."

| 字段 | 值 |
| --- | --- |
| Issue | [#3306](https://github.com/vllm-project/vllm/issues/3306) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> flash_attn is installed, but "flash_attn is not found. Using xformers backend."

### Issue 正文摘录

```bash >>> flash_attn is not found. Using xformers backend. ``` but flash_attn has been added into the vllm wheel ```bash adding 'vllm/thirdparty_files/flash_attn/ops/triton/rotary.py' adding 'vllm/thirdparty_files/flash_attn/ops/triton/__pycache__/__init__.cpython-310.pyc' adding 'vllm/thirdparty_files/flash_attn/ops/triton/__pycache__/cross_entropy.cpython-310.pyc' adding 'vllm/thirdparty_files/flash_attn/ops/triton/__pycache__/k_activations.cpython-310.pyc' adding 'vllm/thirdparty_files/flash_attn/ops/triton/__pycache__/layer_norm.cpython-310.pyc' adding 'vllm/thirdparty_files/flash_attn/ops/triton/__pycache__/linear.cpython-310.pyc' adding 'vllm/thirdparty_files/flash_attn/ops/triton/__pycache__/mlp.cpython-310.pyc' adding 'vllm/thirdparty_files/flash_attn/ops/triton/__pycache__/rotary.cpython-310.pyc' adding 'vllm/thirdparty_files/flash_attn/utils/__init__.py' adding 'vllm/thirdparty_files/flash_attn/utils/benchmark.py' adding 'vllm/thirdparty_files/flash_attn/utils/distributed.py' adding 'vllm/thirdparty_files/flash_attn/utils/generation.py' adding 'vllm/thirdparty_files/flash_attn/utils/pretrained.py' adding 'vllm/thirdparty_files/flash_attn/utils/__pycache__/__init__.cpyt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: flash_attn is installed, but "flash_attn is not found. Using xformers backend." ```bash >>> flash_attn is not found. Using xformers backend. ``` but flash_attn has been added into the vllm wheel ```bash adding 'vllm/thi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: flash_attn is installed, but "flash_attn is not found. Using xformers backend." ```bash >>> flash_attn is not found. Using xformers backend. ``` but flash_attn has been added into the vllm wheel ```bash adding 'vllm/thi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: h_attn/utils/__init__.py' adding 'vllm/thirdparty_files/flash_attn/utils/benchmark.py' adding 'vllm/thirdparty_files/flash_attn/utils/distributed.py' adding 'vllm/thirdparty_files/flash_attn/utils/generation.py' adding...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
