# vllm-project/vllm#15461: [Doc]: https://docs.vllm.ai/en/latest/deployment/k8s.html not working

| 字段 | 值 |
| --- | --- |
| Issue | [#15461](https://github.com/vllm-project/vllm/issues/15461) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: https://docs.vllm.ai/en/latest/deployment/k8s.html not working

### Issue 正文摘录

### 📚 The doc issue Hi I´m following the CPU deployment but this should apply to GPU too: When I start the deployment the container fails after attaching to the PVC and pulling the model with the following error: ``` % oc -n vllm-manual get pod NAME READY STATUS RESTARTS AGE vllm-server-f5c67d786-f9n4f 0/1 CrashLoopBackOff 4 (53s ago) 2m35s % oc -n vllm-manual logs vllm-server-f5c67d786-f9n4f /bin/sh: 1: vllm: Permission denied ``` Running the Deployment with -c "sleep 3600" I find the following inside the container: ``` % oc -n vllm-manual exec -it vllm-server-54cc57c779-g8g5n -- /bin/sh $ which vllm /opt/venv/bin/vllm $ vllm /bin/sh: 2: vllm: Permission denied $ ls -l /opt/venv/bin/vllm -rwxr-xr-x. 1 root root 312 Mar 19 20:53 /opt/venv/bin/vllm $ file /opt/venv/bin/vllm /bin/sh: 4: file: Permission denied $ cat /opt/venv/bin/vllm #!/opt/venv/bin/python3 # -*- coding: utf-8 -*- import sys from vllm.entrypoints.cli.main import main if __name__ == "__main__": if sys.argv[0].endswith("-script.pyw"): sys.argv[0] = sys.argv[0][:-11] elif sys.argv[0].endswith(".exe"): sys.argv[0] = sys.argv[0][:-4] sys.exit(main()) /opt/venv/bin/python3 /bin/sh: 9: /opt/venv/bin/python3: Permission de...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: $ cat /opt/venv/bin/vllm #!/opt/venv/bin/python3 # -*- coding: utf-8 -*- import sys from vllm.entrypoints.cli.main import main if __name__ == "__main__": if sys.argv[0].endswith("-script.pyw"): sys.argv[0] = sys.argv[0]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eployment the container fails after attaching to the PVC and pulling the model with the following error: ``` % oc -n vllm-manual get pod NAME READY STATUS RESTARTS AGE vllm-server-f5c67d786-f9n4f 0/1 CrashLoopBackOff 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s://docs.vllm.ai/en/latest/deployment/k8s.html not working documentation;stale ### 📚 The doc issue Hi I´m following the CPU deployment but this should apply to GPU too: When I start the deployment the container fails af...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Doc]: https://docs.vllm.ai/en/latest/deployment/k8s.html not working documentation;stale ### 📚 The doc issue Hi I´m following the CPU deployment but this should apply to GPU too: When I start the deployment the contain...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
