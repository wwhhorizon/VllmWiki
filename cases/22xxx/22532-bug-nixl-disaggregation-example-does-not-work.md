# vllm-project/vllm#22532: [Bug]: NIXL disaggregation example does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#22532](https://github.com/vllm-project/vllm/issues/22532) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NIXL disaggregation example does not work

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Host: ubuntu, x64, 8xNVidia H200 I've installed VLLM in a venv the following way: ``` git clone https://github.com/vllm-project/vllm cd vllm VLLM_USE_PRECOMPILED=1 uv pip install --editable . -v ``` And LMCache: ``` git clone https://github.com/LMCache/LMCache cd LMCache/ uv pip install -e . -v ``` Then I went to `vllm/examples/others/lmcache/disagg_prefill_lmcache_v1`, [as described here](https://github.com/vllm-project/vllm/blob/main/examples/others/lmcache/README.md) `bash disagg_example_nixl.sh` The example failed with the following error: ``` (EngineCore_0 pid=1147865) [2025-08-08 17:42:35,121] LMCache INFO: Loading LMCache config file /home/minio/piotr/rv/vllm/examples/others/lmcache/disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml (utils.py:57:lmcache.integration.vllm.utils) (EngineCore_0 pid=1147865) [2025-08-08 17:42:35,122] LMCache WARNING: nixl_peer_host is deprecated, use nixl_receiver_host instead (source: file: /home/minio/piotr/rv/vllm/examples/others/lmcache/disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml) (config.py:226:lmcache.v1.config) (EngineCore_0 pid=1147865) [2025-08-08 17:42:35,...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: NIXL disaggregation example does not work bug;stale ### Your current environment ### 🐛 Describe the bug Host: ubuntu, x64, 8xNVidia H200 I've installed VLLM in a venv the following way: ``` git clone https://gith...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nment ### 🐛 Describe the bug Host: ubuntu, x64, 8xNVidia H200 I've installed VLLM in a venv the following way: ``` git clone https://github.com/vllm-project/vllm cd vllm VLLM_USE_PRECOMPILED=1 uv pip install --editable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e_0 pid=1147865) [2025-08-08 17:42:35,121] LMCache INFO: Loading LMCache config file /home/minio/piotr/rv/vllm/examples/others/lmcache/disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml (utils.py:57:lmcache.i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
