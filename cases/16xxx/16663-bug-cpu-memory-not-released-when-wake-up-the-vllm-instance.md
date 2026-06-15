# vllm-project/vllm#16663: [Bug]: cpu memory not released when wake up the vLLM instance

| 字段 | 值 |
| --- | --- |
| Issue | [#16663](https://github.com/vllm-project/vllm/issues/16663) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cpu memory not released when wake up the vLLM instance

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug model weights offloads to cpu memory when called /sleep api. But after call /wake_up api, the cpu memory do not release. Is this on purpose to fast sleep vllm engine for the next time? In multi model switching scenario, this could bring big pressure on cpu memory for each slept model still occupy cpu memory. ``` [root@host ~]# free -h total used free shared buff/cache available Mem: 225Gi 4.1Gi 174Gi 21Mi 46Gi 219Gi Swap: 63Gi 245Mi 63Gi [root@host ~]# curl -XPOST http://localhost:8090/sleep?level=1 [root@host ~]# curl http://localhost:8090/is_sleeping {"is_sleeping":true} [root@host ~]# free -h total used free shared buff/cache available Mem: 225Gi 5.3Gi 124Gi 49Gi 96Gi 169Gi Swap: 63Gi 245Mi 63Gi [root@host ~]# curl -XPOST http://localhost:8090/wake_up [root@host ~]# curl http://localhost:8090/is_sleeping {"is_sleeping":false} [root@host ~]# free -h total used free shared buff/cache available Mem: 225Gi 5.3Gi 124Gi 49Gi 96Gi 169Gi Swap: 63Gi 245Mi 63Gi ``` when check the memory of progress, it seems many deleted /dev/zero file handle. ``` [root@host ~]# ps aux | grep spawn root 198907 1.4 22.7 161240136 53878080 pts/0 Sl+ 16:27...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 80 pts/0 Sl+ 16:27 4:14 /usr/bin/python3 -c from multiprocessing.spawn import spawn_main; spawn_main(tracker_fd=16, pipe_handle=18) --multiprocessing-fork [root@host ~]# lsof -p 198907 | wc -l 485 [root@host ~]# lsof -p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0,1 27134 /dev/zero ... [root@host ~]# cat /proc/198907/smaps ... 7f42c0000000-7f42e0000000 rw-s 00000000 00:01 28385 /dev/zero (deleted) Size: 524288 kB KernelPageSize: 4 kB MMUPageSize: 4 kB Rss: 524288 kB Pss:
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tance bug;stale ### Your current environment ### 🐛 Describe the bug model weights offloads to cpu memory when called /sleep api. But after call /wake_up api, the cpu memory do not release. Is this on purpose to fast sle...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e ### Your current environment ### 🐛 Describe the bug model weights offloads to cpu memory when called /sleep api. But after call /wake_up api, the cpu memory do not release. Is this on purpose to fast sleep vllm engine...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
