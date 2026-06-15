# vllm-project/vllm#17015: [Installation]:  Cannot install vllm due to xformers:   ERROR: Failed building wheel for xformers  fatal: Not a git repository (or any parent up to mount point /scratch)  assert len(sources) > 0   AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#17015](https://github.com/vllm-project/vllm/issues/17015) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | activation;attention;cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]:  Cannot install vllm due to xformers:   ERROR: Failed building wheel for xformers  fatal: Not a git repository (or any parent up to mount point /scratch)  assert len(sources) > 0   AssertionError

### Issue 正文摘录

Hi all, I am pip installing the latest vllm, 0.8.4. CUDA: 12.4 torch: 2.6.0 Python: 3.12.1 ```text The output of `python collect_env.py` ``` python collect_env.py Traceback (most recent call last): File "/program/ms-swift/collect_env.py", line 17, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm' I got several errors: ERROR: Failed building wheel for xformers fatal: Not a git repository (or any parent up to mount point /scratch) assert len(sources) > 0 AssertionError Error logs: ---------------------------------------- (myvenv_msswift) [data@sh1 /program//ms-swift] $ pip install xformers Collecting xformers Using cached xformers-0.0.29.post3.tar.gz (8.5 MB) Preparing metadata (setup.py) ... done Building wheels for collected packages: xformers Building wheel for xformers (setup.py) ... error error: subprocess-exited-with-error × python setup.py bdist_wheel did not run successfully. │ exit code: 1 ╰─> [257 lines of output] fatal: Not a git repository (or any parent up to mount point /scratch) Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set). /program//myvenv_msswift/lib/python3.12/site-packages/setuptools/dist.py:759...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Cannot install vllm due to xformers: ERROR: Failed building wheel for xformers fatal: Not a git repository (or any parent up to mount point /scratch) assert len(sources) > 0 AssertionError installat
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: -312/xformers/ops/_triton copying xformers/ops/_triton/matmul_perf_model.py -> build/lib.linux-x86_64-cpython-312/xformers/ops/_triton creating build/lib.linux-x86_64-cpython-312/xformers/ops/fmha/_triton copying xforme...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rs/benchmarks creating build/lib.linux-x86_64-cpython-312/xformers/triton copying xformers/triton/__init__.py -> build/lib.linux-x86_64-cpython-312/xformers/triton copying xformers/triton/importing.py -> build/lib.linux...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ormers Using cached xformers-0.0.29.post3.tar.gz (8.5 MB) Preparing metadata (setup.py) ... done Building wheels for collected packages: xformers Building wheel for xformers (setup.py) ... error error: subprocess-exited...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t point /scratch) assert len(sources) > 0 AssertionError installation;stale Hi all, I am pip installing the latest vllm, 0.8.4. CUDA: 12.4 torch: 2.6.0 Python: 3.12.1 ```text The output of `python collect_env.py` ``` py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
