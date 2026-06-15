# vllm-project/vllm#7511: [Bug]: Docker.xpu  build failed

| 字段 | 值 |
| --- | --- |
| Issue | [#7511](https://github.com/vllm-project/vllm/issues/7511) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Docker.xpu  build failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I build docker.xpu following https://docs.vllm.ai/en/latest/getting_started/xpu-installation.html. I met the error. > [6/8] RUN pip install -v -r requirements-xpu.txt: 1.262 Non-user install because site-packages writeable 1.358 Created temporary directory: /tmp/pip-ephem-wheel-cache-hsg1xl66 1.358 Created temporary directory: /tmp/pip-req-tracker-56wczsdx 1.359 Initialized build tracking at /tmp/pip-req-tracker-56wczsdx 1.359 Created build tracker: /tmp/pip-req-tracker-56wczsdx 1.359 Entered build tracker: /tmp/pip-req-tracker-56wczsdx 1.359 Created temporary directory: /tmp/pip-install-zgyc7tj8 1.381 Cleaning up... 1.381 Removed build tracker: '/tmp/pip-req-tracker-56wczsdx' 1.381 ERROR: torch-2.1.0.post1+cxx11.abi-cp310-cp310-linux_x86_64.whl is not a supported wheel on this platform. 1.382 Exception information: 1.382 Traceback (most recent call last): 1.382 File "/usr/lib/python3/dist-packages/pip/_internal/cli/base_command.py", line 186, in _main 1.382 status = self.run(options, args) 1.382 File "/usr/lib/python3/dist-packages/pip/_internal/commands/install.py", line 325, in run 1.382 self.populate_requirement_set( 1.3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Docker.xpu build failed bug;stale ### Your current environment ### 🐛 Describe the bug When I build docker.xpu following https://docs.vllm.ai/en/latest/getting_started/xpu-installation.html. I met the error. > [6/
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _x86_64.whl is not a supported wheel on this platform. 1.382 Exception information: 1.382 Traceback (most recent call last): 1.382 File "/usr/lib/python3/dist-packages/pip/_internal/cli/base_command.py", line 186, in _m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Docker.xpu build failed bug;stale ### Your current environment ### 🐛 Describe the bug When I build docker.xpu following https://docs.vllm.ai/en/latest/getting_started/xpu-installation.html. I met the error. > [6/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ibe the bug When I build docker.xpu following https://docs.vllm.ai/en/latest/getting_started/xpu-installation.html. I met the error. > [6/8] RUN pip install -v -r requirements-xpu.txt:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
