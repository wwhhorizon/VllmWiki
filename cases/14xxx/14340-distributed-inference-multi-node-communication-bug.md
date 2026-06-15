# vllm-project/vllm#14340: distributed inference multi-node communication bug

| 字段 | 值 |
| --- | --- |
| Issue | [#14340](https://github.com/vllm-project/vllm/issues/14340) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> distributed inference multi-node communication bug

### Issue 正文摘录

> i set NCCL_SOCKET_IFNAME and GLOO_SOCKET_IFNAME，then run run_cluster.sh > > ``` > # master > bash run_cluster.sh vllm/vllm-openai xx.xx.xx.12 --head /root/path -e VLLM_HOST_IP=xx.xx.xx.12 -e NCCL_SOCKET_IFNAME=ens49f0 -e GLOO_SOCKET_IFNAME=ens49f0 > > # work > bash run_cluster.sh vllm/vllm-openai xx.xx.xx.12 --worker /root/path -e VLLM_HOST_IP=xx.xx.xx.15 -e NCCL_SOCKET_IFNAME=ens49f0 -e GLOO_SOCKET_IFNAME=ens49f0 > ``` > > then run ` > NCCL_DEBUG=TRACE torchrun --nnodes 2 --nproc-per-node=8 --rdzv_backend=c10d --rdzv_endpoint=xx.xx.xx.12 test.py` > > result is > ``` > W0306 00:02:25.387000 473 torch/distributed/run.py:793] > W0306 00:02:25.387000 473 torch/distributed/run.py:793] ***************************************** > W0306 00:02:25.387000 473 torch/distributed/run.py:793] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. > W0306 00:02:25.387000 473 torch/distributed/run.py:793] ***************************************** > [E306 00:03:07.842961975 socket.cpp:1011] [c10d] The client socket has timed out after 60000ms w...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ``` > > my env > ``` > Collecting environment information... > PyTorch version: 2.5.1+cu124 > Is debug build: False > CUDA used to build PyTorch: 12.4 > ROCM used to build PyTorch: N/A > > OS: Ubuntu 22.04.3 LTS (x86_64...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: n run ` > NCCL_DEBUG=TRACE torchrun --nnodes 2 --nproc-per-node=8 --rdzv_backend=c10d --rdzv_endpoint=xx.xx.xx.12 test.py` > > result is > ``` > W0306 00:02:25.387000 473 torch/distributed/run.py:793] > W0306 00:02:25.3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 9: Py_RunMain + 0x2e8 (0x658008 in /usr/bin/python3) > frame #30: Py_BytesMain + 0x2d (0x61143d in /usr/bin/python3) > frame #31: + 0x29d90 (0x7fbd9635dd90 in /usr/lib/x86_64-linux-gnu/libc.so.6) > frame #32: __libc_sta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: /launcher/api.py", line 138, in __call__ > return launch_agent(self._config, self._entrypoint, list(args)) > ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ > File "/usr/local/lib/python3.12/dist-packages/torch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: onment information... > PyTorch version: 2.5.1+cu124 > Is debug build: False > CUDA used to build PyTorch: 12.4 > ROCM used to build PyTorch: N/A > > OS: Ubuntu 22.04.3 LTS (x86_64) > GCC version: (Ubuntu 11.4.0-1ubuntu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) > frame #4: <unknown function> + 0x602a3a4 (0x7fbd853903a4 in /usr/local/lib/python3.12/dist-packages/torch/lib/libto… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) > frame #6: c10d::tcpstore::tcpstore(std::string, c10d::tcpstoreoptions const&) + 0x20c (0x7fbd85350f7c in /usr/local… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) > frame #7: <unknown function> + 0xda37d9 (0x7fbd94d3c7d9 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtor… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | /usr/bin/python3) > frame #11: /usr/bin/python3() [0x5a60ae] > frame #12: _pyobject_call + 0xed (0x58a5ad in /usr/bin/python3) > frame #13: /usr/bin/python3() [0x587a15] > frame #… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | al/lib/python3.12/dist-packages/torch/lib/libtorch_python.so) > frame #16: _pyobject_maketpcall + 0x2db (0x547cdb in /usr/bin/python3) > frame #17: _pyeval_evalframedefault + 0x70… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | _pyobject_call_prepend + 0x59 (0x587c99 in /usr/bin/python3) > frame #20: /usr/bin/python3() [0x671a6d] > frame #21: _pyobject_call + 0x93 (0x58a553 in /usr/bin/python3) > frame #… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | /usr/bin/python3) > frame #20: /usr/bin/python3() [0x671a6d] > frame #21: _pyobject_call + 0x93 (0x58a553 in /usr/bin/python3) > frame #22: _pyeval_evalframedefault + 0x54dd (0x55… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | thon3() [0x647ad6] > frame #26: /usr/bin/python3() [0x65fc35] > frame #27: _pyrun_simplefileobject + 0x1a5 (0x65f205 in /usr/bin/python3) > frame #28: _pyrun_anyfileobject + 0x47… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | 8: _pyrun_anyfileobject + 0x47 (0x65ee97 in /usr/bin/python3) > frame #29: py_runmain + 0x2e8 (0x658008 in /usr/bin/python3) > frame #30: py_bytesmain + 0x2d (0x61143d in /usr/bin… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | 29d90 (0x7fbd9635dd90 in /usr/lib/x86_64-linux-gnu/libc.so.6) > frame #32: __libc_start_main + 0x80 (0x7fbd9635de40 in /usr/lib/x86_64-linux-gnu/libc.so.6) > frame #33: _start + 0… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
