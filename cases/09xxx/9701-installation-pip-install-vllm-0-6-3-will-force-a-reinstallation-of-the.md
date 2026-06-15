# vllm-project/vllm#9701: [Installation] pip install vllm (0.6.3) will force a reinstallation of the CPU version torch and replace cuda torch on windows

| 字段 | 值 |
| --- | --- |
| Issue | [#9701](https://github.com/vllm-project/vllm/issues/9701) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 50; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation] pip install vllm (0.6.3) will force a reinstallation of the CPU version torch and replace cuda torch on windows

### Issue 正文摘录

pip install vllm (0.6.3) will force a reinstallation of the CPU version torch and replace cuda torch on windows. pip install vllm（0.6.3）将强制重新安装CPU版本的torch并在Windows上替换cuda torch。 > > > > > > I don't quite get what you mean, how can you have different versions of torch for CPU and GPU at the same time?我不太明白你的意思，你怎么能有不同版本的火炬CPU和GPU在同一时间？ > > only cuda torch > > ``` > pip install vllm --no-deps > Collecting vllm > Using cached vllm-0.6.3.post1.tar.gz (2.7 MB) > Installing build dependencies ... error > error: subprocess-exited-with-error > > × pip subprocess to install build dependencies did not run successfully. > │ exit code: 2 > ╰─> [86 lines of output] > Collecting cmake>=3.26 > Using cached cmake-3.30.5-py3-none-win_amd64.whl.metadata (6.4 kB) > Collecting ninja > Using cached ninja-1.11.1.1-py2.py3-none-win_amd64.whl.metadata (5.4 kB) > > Collecting packaging > Using cached packaging-24.1-py3-none-any.whl.metadata (3.2 kB) > Collecting setuptools>=61 > Using cached setuptools-75.2.0-py3-none-any.whl.metadata (6.9 kB) > Collecting setuptools-scm>=8.0 > Using cached setuptools_scm-8.1.0-py3-none-any.whl.metadata (6.6 kB) > Collecting torch==2.4.0 > Using cached torch-2.4.0-cp310-c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation] pip install vllm (0.6.3) will force a reinstallation of the CPU version torch and replace cuda torch on windows installation;stale pip install vllm (0.6.3) will force a reinstallation of the CPU version t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: g cmake>=3.26 > Using cached cmake-3.30.5-py3-none-win_amd64.whl.metadata (6.4 kB) > Collecting ninja > Using cached ninja-1.11.1.1-py2.py3-none-win_amd64.whl.metadata (5.4 kB) > > Collecting packaging > Using cached pa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: of the CPU version torch and replace cuda torch on windows installation;stale pip install vllm (0.6.3) will force a reinstallation of the CPU version torch and replace cuda torch on windows. pip install vllm（0.6.3）将强制重新...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: um, peft, stable-baselines3, timm, t orchaudio, torchvision, trl, vector-quantize-pytorch, vocos development attention_kv_cache;ci_build;frontend_api;quantization cuda;quantization build_error;crash env_dependency pip i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: (0.6.3) will force a reinstallation of the CPU version torch and replace cuda torch on windows installation;stale pip install vllm (0.6.3) will force a reinstallation of the CPU version torch and replace cuda torch on w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
