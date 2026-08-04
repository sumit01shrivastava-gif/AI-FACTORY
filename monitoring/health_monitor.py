class HealthMonitor:

    def status(self):

        return {
            "memory": "healthy",
            "database": "healthy",
            "queue": "healthy",
            "sandbox": "healthy",
        }
