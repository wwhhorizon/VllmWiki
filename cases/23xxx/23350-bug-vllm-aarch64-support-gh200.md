# vllm-project/vllm#23350: [Bug]: vLLM aarch64 support (GH200)

| 字段 | 值 |
| --- | --- |
| Issue | [#23350](https://github.com/vllm-project/vllm/issues/23350) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM aarch64 support (GH200)

### Issue 正文摘录

### Your current environment Cannot install VLLM ```text Traceback (most recent call last): File "/lus/lfs1aip2/home/brics/akawafi1.brics/repos/test/vllm/collect_env.py", line 19, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm.envs' ``` ### 🐛 Describe the bug Hello, we need to run `0.10.1+gptoss` but it is not supported on GH200. I have tried torch 2.6 (cuda126) and 2.7 (cuda128) ```shell $ uv pip install --pre vllm==0.10.1+gptoss --extra-index-url https://wheels.vllm.ai/gpt-oss/ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 --index-strategy unsafe-best-match Using Python 3.12.11 environment at: /home/brics/akawafi1.brics/miniforge3/envs/vllm_env × No solution found when resolving dependencies: ╰─▶ Because vllm==0.10.1+gptoss has no wheels with a matching platform tag (e.g., `manylinux_2_31_aarch64`) and you require vllm==0.10.1+gptoss, we can conclude that your requirements are unsatisfiable. hint: Wheels are available for `vllm` (v0.10.1+gptoss) on the following platform: `linux_x86_64` ``` Trying to build from source results in the following errors despite having cudatoolkit available: ``` module load cudatoolkit con...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: M aarch64 support (GH200) bug;stale ### Your current environment Cannot install VLLM ```text Traceback (most recent call last): File "/lus/lfs1aip2/home/brics/akawafi1.brics/repos/test/vllm/collect_env.py", line 19, in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: vLLM aarch64 support (GH200) bug;stale ### Your current environment Cannot install VLLM ```text Traceback (most recent call last): File "/lus/lfs1aip2/home/brics/akawafi1.brics/repos/test/vllm/collect_env.py", li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: l --pre vllm==0.10.1+gptoss --extra-index-url https://wheels.vllm.ai/gpt-oss/ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 --index-strategy unsafe-best-match Using Python 3.12.11 environment at: /hom...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vLLM aarch64 support (GH200) bug;stale ### Your current environment Cannot install VLLM ```text Traceback (most recent call last): File "/lus/lfs1aip2/home/brics/akawafi1.brics/repos/test/vllm/collect_env.py", li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: recent call last): File "/lus/lfs1aip2/home/brics/akawafi1.brics/repos/test/vllm/collect_env.py", line 19, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm.envs' ``` ### 🐛 Descri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
